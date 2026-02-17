# Custom Preview Domain for PRs

> **🌐 Access your PR previews at a memorable custom domain:** `preview-startup-blueprint.SuperiorByteWorks.com`

This feature automatically configures a custom domain for PR preview deployments, making them easier to share and test.

---

## ✨ Features

- **Custom Domain**: All preview deployments with the `Deploy: Website Preview` label are accessible at `https://preview-startup-blueprint.SuperiorByteWorks.com`
- **Automatic DNS Management**: CNAME records are automatically created/updated
- **Clean Transitions**: Old domain assignments are removed before adding new ones
- **Conflict Detection**: Warns when multiple PRs have the preview label
- **Fallback URL**: Direct Cloudflare Pages URLs remain available

---

## 🔑 Prerequisites

### Cloudflare API Token Permissions

Your `CLOUDFLARE_API_TOKEN` must have these exact permissions:

| Permission                     | Type | Purpose                          |
| ------------------------------ | ---- | -------------------------------- |
| **Account → Cloudflare Pages** | Edit | Deploy to Pages, manage projects |
| **Zone → DNS**                 | Edit | Create/update CNAME records      |
| **Zone → Zone**                | Read | Find Zone ID for domain          |

#### How to Create the Token (Step by Step)

1. **Go to Cloudflare Dashboard:**
   - Visit [dash.cloudflare.com](https://dash.cloudflare.com)
   - Log in to your account

2. **Navigate to API Tokens:**
   - Click your profile icon (top-right)
   - Select "My Profile"
   - Click "API Tokens" in the left sidebar

3. **Create Custom Token:**
   - Click **"Create Custom Token"**
   - Name: `GitHub-Actions-Deploy`

4. **Set Permissions (exactly as shown below):**

   Click "Add +" and add each row:

   | Permission | Type             |
   | ---------- | ---------------- | ---- |
   | Account    | Cloudflare Pages | Edit |
   | Zone       | DNS              | Edit |
   | Zone       | Zone             | Read |

   Your permissions should look like:

   ```
   - Account:Cloudflare Pages:Edit
   - Zone:DNS:Edit
   - Zone:Zone:Read
   ```

5. **Configure Token Settings:**
   - **Account Resources**: Include your account (dropdown)
   - **Zone Resources**: Include All Zones (dropdown)
   - **TTL**: Never expire (or set to 1 year)

6. **Create and Copy:**
   - Click "Continue to summary"
   - Click "Create Token"
   - **IMPORTANT**: Copy the token NOW - you won't see it again!
   - Save it somewhere safe (you'll add it to GitHub Secrets)

#### How to Verify Token Works

```bash
# Test your token
curl -X GET "https://api.cloudflare.com/client/v4/user/tokens/verify" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json"
```

Expected response: `{"success": true, "result": {"id": "...", "name": "GitHub-Actions-Deploy", ...}}`

#### How to Get Your Account ID

1. In Cloudflare Dashboard, look at the URL:
   - `https://dash.cloudflare.com/ACCOUNT_ID_HERE`
   - Copy the alphanumeric string in the URL

2. Or go to:
   - Click your profile icon
   - Select "My Profile"
   - Scroll down to "Account ID"

---

## 🚀 How It Works

### Workflow

1. **PR is opened** with the `Deploy: Website Preview` label
2. **Build completes** and creates a Cloudflare Pages deployment
3. **Domain script runs** (`scripts/cloudflare/manage-preview-domain.sh`):
   - Finds Zone ID for `SuperiorByteWorks.com`
   - **Removes** `preview-startup-blueprint` domain from ALL Pages projects
   - **Adds** `preview-startup-blueprint.SuperiorByteWorks.com` to the current deployment
   - **Creates/updates** DNS CNAME record pointing to `startup-blueprint.pages.dev`
4. **PR comment** shows both custom domain and direct URL
5. **DNS propagates** (1-2 minutes)
6. **Preview accessible** at custom domain

### One Label at a Time ⚠️

**Important**: Only **ONE** PR should have the `Deploy: Website Preview` label at a time.

**Why?** The custom domain can only point to one deployment. If multiple PRs have the label:

- The custom domain will point to whichever deployed **most recently**
- Other PRs will still have their direct Cloudflare URLs
- A warning will be posted on all conflicting PRs

**Recommended Process**:

1. Remove the label from PR A when you want to preview PR B
2. Add the label to PR B
3. Wait for PR B to deploy and configure the custom domain

---

## 📝 Usage

### For Developers

#### Deploy Your PR to Preview Domain

1. **Open a pull request**
2. **Add the label**: `Deploy: Website Preview`
3. **Wait for deployment** (usually 3-5 minutes)
4. **Check the PR comment** for the custom domain URL
5. **Access your preview** at `https://preview-startup-blueprint.SuperiorByteWorks.com`

#### Switch Preview to Another PR

1. **Remove the label** from the current PR
2. **Add the label** to the new PR
3. The workflow will automatically:
   - Remove the domain from the old deployment
   - Add it to the new deployment
   - Update DNS (if needed)

### For Reviewers

- **Look for the PR comment** with the custom domain link
- **Click the custom domain** to preview the changes
- If the custom domain isn't working:
  - Check DNS propagation (1-2 minutes)
  - Use the direct Cloudflare URL as fallback
  - Check for label conflicts (warning comment)

---

## 🔧 Architecture

### Files

```
├── .github/workflows/
│   ├── preview-deploy-reusable.yml          # Calls domain script after deployment
│   └── check-preview-label-conflict.yml    # Detects multiple PRs with label
├── scripts/cloudflare/
│   └── manage-preview-domain.sh            # Domain/DNS management script
└── docs/
    └── preview-deployment-custom-domain.md # This document
```

### Domain Management Script

**Location**: `scripts/cloudflare/manage-preview-domain.sh`

**What it does**:

1. Validates environment variables (`CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`)
2. Finds Zone ID for `SuperiorByteWorks.com`
3. Loops through **all** Cloudflare Pages projects
4. Removes `preview-startup-blueprint.SuperiorByteWorks.com` from any project that has it
5. Adds the custom domain to the **current** project
6. Creates or updates DNS CNAME record

**Idempotent**: Safe to run multiple times

**Error Handling**: Exits with code 1 on failure, logs detailed error messages

### Cloudflare API Calls

| API Endpoint                              | Purpose                  | HTTP Method |
| ----------------------------------------- | ------------------------ | ----------- |
| `/zones?name=SuperiorByteWorks.com`       | Get Zone ID              | GET         |
| `/pages/projects`                         | List all Pages projects  | GET         |
| `/pages/projects/{name}/domains`          | List domains for project | GET         |
| `/pages/projects/{name}/domains/{domain}` | Remove custom domain     | DELETE      |
| `/pages/projects/{name}/domains`          | Add custom domain        | POST        |
| `/zones/{zone}/dns_records?type=CNAME`    | Find existing DNS record | GET         |
| `/zones/{zone}/dns_records/{id}`          | Update DNS record        | PUT         |
| `/zones/{zone}/dns_records`               | Create DNS record        | POST        |

---

## 🐛 Troubleshooting

### Custom Domain Not Working

**Symptoms**: Visiting `preview-startup-blueprint.SuperiorByteWorks.com` shows an error or wrong content

**Possible Causes**:

1. **DNS Propagation Delay**
   - **Solution**: Wait 1-2 minutes after deployment completes
   - **Check**: Use `dig preview-startup-blueprint.SuperiorByteWorks.com` to verify CNAME

2. **Another PR Has the Label**
   - **Solution**: Check for warning comments on your PR
   - **Fix**: Remove label from other PRs

3. **API Token Missing Permissions**
   - **Solution**: Verify token has Zone.DNS:Edit permission
   - **Check**: Run the token test command from Prerequisites section

4. **Script Failed**
   - **Solution**: Check GitHub Actions logs for the "Configure custom preview domain" step
   - **Look for**: Red X in the workflow run

### DNS Record Conflicts

**Symptoms**: Script fails with "DNS record already exists" error

**Solution**: The script should auto-detect and update existing records. If this fails:

1. Go to [Cloudflare DNS settings](https://dash.cloudflare.com)
2. Find the `preview-startup-blueprint` CNAME record
3. Delete it manually
4. Re-run the workflow

### Multiple PRs Warning

**Symptoms**: Warning comment appears on your PR about label conflicts

**What it means**: Another PR also has the `Deploy: Website Preview` label

**Impact**: The custom domain points to whichever PR deployed **most recently**

**Solution**:

1. Decide which PR should have the custom domain
2. Remove the label from the other PR(s)
3. The warning will automatically be removed

---

## 📊 Monitoring

### Check Domain Assignment

```bash
# Which deployment is the custom domain pointing to?
curl -s -X GET "https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/pages/projects/startup-blueprint/domains" \
  -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" | jq -r '.result[] | select(.name == "preview-startup-blueprint.SuperiorByteWorks.com")'
```

### Check DNS Record

```bash
# What does the DNS record point to?
dig preview-startup-blueprint.SuperiorByteWorks.com CNAME +short
```

Expected output: `startup-blueprint.pages.dev.`

### Check Label Status

```bash
# Which open PRs have the preview label?
gh pr list --label "Deploy: Website Preview" --state open
```

---

## 🛡️ Security Considerations

- **API Token**: Stored as GitHub Secret, never exposed in logs
- **DNS Changes**: Limited to `preview-startup-blueprint` subdomain only
- **Domain Access**: Public (same as regular Cloudflare Pages previews)
- **Rate Limiting**: Cloudflare API rate limits apply (usually 1200 req/5min per token)

---

## 🔗 Related Documentation

- [Cloudflare Pages Custom Domains](https://developers.cloudflare.com/pages/configuration/custom-domains/)
- [Cloudflare API: Pages](https://developers.cloudflare.com/api/operations/pages-project-get-project)
- [Cloudflare API: DNS](https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-list-dns-records)
- [GitHub Actions Workflows](../.github/workflows/README.md)

---

## ❓ FAQ

**Q: Can I use a different custom domain?**  
A: Yes, edit `CUSTOM_DOMAIN` in `scripts/cloudflare/manage-preview-domain.sh`

**Q: Can multiple PRs have separate custom domains?**  
A: Yes, but you'd need separate domains (e.g., `preview-1`, `preview-2`) and update the script to manage them individually

**Q: What happens when the PR is merged?**  
A: The label is removed, triggering cleanup. The custom domain remains but points to the last deployment until another PR adds the label

**Q: How do I disable this feature?**  
A: Remove the "Configure custom preview domain" step from `.github/workflows/preview-deploy-reusable.yml`

**Q: Does this work for production deployments?**  
A: No, this is preview-only. Production uses a different workflow and domain

---

**Last Updated**: 2026-01-24  
**Maintainer**: Clayton Young  
**Status**: ✅ Production-ready
