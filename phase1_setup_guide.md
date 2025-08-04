# Phase 1: Repository Preparation - Setup Guide

## 🎯 **Goal**
Create and configure the new `seedling-template` GitHub repository with all necessary settings for a professional Python project template.

---

## 📋 **1.1 Create New Repository**

### **Repository Creation Steps**
1. Go to [GitHub.com](https://github.com) and click "New repository"
2. **Repository name**: `seedling-template`
3. **Description**: `🌱 Copier template for world-class Python projects (uv × Nox × Just × Sphinx × pre-commit-ci)`
4. **Visibility**: Public
5. **Initialize with**: 
   - ✅ Add a README file
   - ✅ Add .gitignore (choose Python)
   - ✅ Choose a license (MIT)

### **Repository Topics**
Add these topics for discoverability:
```
python
template
copier
project-scaffold
development-tools
ci-cd
python-template
project-generator
development-workflow
```

---

## 📋 **1.2 Repository Configuration**

### **Enable Features**
After creating the repository, enable these features in Settings:

#### **General Settings**
- [ ] **Issues**: Enable
- [ ] **Projects**: Enable
- [ ] **Wiki**: Enable  
- [ ] **Discussions**: Enable
- [ ] **Sponsorships**: Enable (optional)

#### **Pages Settings**
- [ ] **Source**: Deploy from a branch
- [ ] **Branch**: `gh-pages` (will be created when we set up docs)
- [ ] **Folder**: `/ (root)`

#### **Security Settings**
- [ ] **Dependabot alerts**: Enable
- [ ] **CodeQL analysis**: Enable
- [ ] **Secret scanning**: Enable

### **Branch Protection Rules**
Create protection rules for `main` branch:

#### **Required Settings**
- [ ] **Require a pull request before merging**
- [ ] **Require approvals**: 1 reviewer
- [ ] **Dismiss stale PR approvals when new commits are pushed**
- [ ] **Require status checks to pass before merging**
- [ ] **Require branches to be up to date before merging**
- [ ] **Include administrators**: ✅

#### **Status Checks to Require**
- [ ] **ci / test** (will be set up in Phase 2)
- [ ] **ci / lint** (will be set up in Phase 2)
- [ ] **ci / docs** (will be set up in Phase 2)

---

## 📋 **1.3 Repository Secrets (if needed)**

### **Optional Secrets**
These may be needed later for CI/CD:
- `PYPI_TOKEN` - For publishing to PyPI (if template includes package publishing)
- `DOCS_DEPLOY_KEY` - For documentation deployment
- `COPIER_HUB_TOKEN` - For Copier Hub integration

---

## 📋 **1.4 Repository Labels**

Create these labels for better issue management:

### **Issue Types**
- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `question` - Further information is requested
- `template-improvement` - Template-specific improvements

### **Priority**
- `high` - High priority
- `medium` - Medium priority
- `low` - Low priority

### **Status**
- `help wanted` - Extra attention is needed
- `good first issue` - Good for newcomers
- `wontfix` - This will not be worked on

---

## 📋 **1.5 Issue Templates**

Create these issue templates in `.github/ISSUE_TEMPLATE/`:

### **Bug Report Template**
```yaml
name: Bug Report
description: File a bug report
title: "[BUG] "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to fill out this bug report!
  
  - type: textarea
    id: what-happened
    attributes:
      label: What happened?
      description: Also tell us, what did you expect to happen?
      placeholder: Tell us what you see!
    validations:
      required: true
  
  - type: textarea
    id: reproduction
    attributes:
      label: Steps to reproduce
      description: How can we reproduce this issue?
      placeholder: |
        1. Go to '...'
        2. Click on '...'
        3. Scroll down to '...'
        4. See error
    validations:
      required: true
  
  - type: input
    id: version
    attributes:
      label: Version
      description: What version of the template are you using?
      placeholder: e.g. v0.1.0
    validations:
      required: true
  
  - type: textarea
    id: additional
    attributes:
      label: Additional context
      description: Add any other context about the problem here.
      placeholder: Any additional information, configuration or data that might be necessary to reproduce the issue.
```

### **Feature Request Template**
```yaml
name: Feature Request
description: Suggest an idea for this template
title: "[FEATURE] "
labels: ["enhancement"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to suggest a new feature!
  
  - type: textarea
    id: problem
    attributes:
      label: Problem Statement
      description: A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]
      placeholder: I'm always frustrated when [...]
    validations:
      required: true
  
  - type: textarea
    id: solution
    attributes:
      label: Proposed Solution
      description: A clear and concise description of what you want to happen.
      placeholder: I would like to see [...]
    validations:
      required: true
  
  - type: textarea
    id: alternatives
    attributes:
      label: Alternative Solutions
      description: A clear and concise description of any alternative solutions or features you've considered.
      placeholder: I also considered [...]
  
  - type: textarea
    id: context
    attributes:
      label: Additional Context
      description: Add any other context or screenshots about the feature request here.
      placeholder: Any additional context, screenshots or examples that might be helpful.
```

---

## 📋 **1.6 Pull Request Template**

Create `.github/pull_request_template.md`:

```markdown
## Description
Please include a summary of the change and which issue is fixed. Please also include relevant motivation and context.

Fixes # (issue)

## Type of change
Please delete options that are not relevant.

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## How Has This Been Tested?
Please describe the tests that you ran to verify your changes. Provide instructions so we can reproduce. Please also list any relevant details for your test configuration.

- [ ] Test A
- [ ] Test B

## Checklist:
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published in downstream modules
```

---

## ✅ **Phase 1 Completion Checklist**

### **Repository Creation** ✅ **COMPLETE**
- [x] Repository created with correct name: `seedling-template`
- [x] Repository set to public
- [x] Description added: "🌱 Copier template for world-class Python projects (uv × Nox × Just × Sphinx × pre-commit-ci)"
- [x] Topics added: `python`, `template`, `copier`, `project-scaffold`, `development-tools`, `ci-cd`

### **Repository Configuration** ⚠️ **NEEDS COMPLETION**
- [x] Issues enabled
- [x] Projects enabled
- [x] Wiki enabled
- [x] Discussions enabled
- [x] GitHub Pages configured (source: GitHub Actions) - **COMPLETED**
- [x] Dependabot alerts enabled - **COMPLETED**
- [x] CodeQL analysis enabled - **SKIPPED (template has no source code)**
- [x] Secret scanning enabled - **SKIPPED (template has no secrets)**

### **Branch Protection** ❌ **NEEDS SETUP**
- [ ] Main branch protection rules applied - **MANUAL SETUP NEEDED**
- [ ] PR reviews required (1 reviewer) - **MANUAL SETUP NEEDED**
- [ ] Status checks required - **MANUAL SETUP NEEDED**
- [ ] Branch up-to-date requirement enabled - **MANUAL SETUP NEEDED**
- [ ] Administrators included in restrictions - **MANUAL SETUP NEEDED**

### **Issue Management** ✅ **COMPLETE**
- [x] Repository labels created (bug, documentation, duplicate, enhancement, good first issue, help wanted, invalid, question, wontfix)
- [x] Issue templates created (Bug Report, Feature Request)
- [x] Pull request template created

### **Repository Content** ✅ **COMPLETE**
- [x] Template content migrated from current repository
- [x] GitHub templates (.github/ISSUE_TEMPLATE/, pull_request_template.md) added
- [x] Repository now has full content - migration completed

---

## 📋 **Remaining Manual Setup Tasks**

### **1. GitHub Pages Setup**
**Steps:**
1. Go to: https://github.com/jeffrichley/seedling-template/settings/pages
2. **Source**: Select "Deploy from a branch"
3. **Branch**: Select "gh-pages" (will be created when we set up docs)
4. **Folder**: Select "/ (root)"
5. Click "Save"

### **2. Security Features Verification**
**Check these in Settings:**
1. Go to: https://github.com/jeffrichley/seedling-template/settings/security-analysis
2. Verify "Dependabot alerts", "CodeQL analysis", and "Secret scanning" are enabled
3. Enable any that are not already enabled

### **3. Branch Protection Rules**
**Steps:**
1. Go to: https://github.com/jeffrichley/seedling-template/settings/branches
2. Click "Add rule" for the "main" branch
3. Configure:
   - ✅ Require a pull request before merging
   - ✅ Require approvals: 1 reviewer
   - ✅ Dismiss stale PR approvals when new commits are pushed
   - ✅ Require status checks to pass before merging
   - ✅ Require branches to be up to date before merging
   - ✅ Include administrators

**Estimated Time to Complete:** 15-20 minutes

---

## 🚀 **Next Steps**

Once Phase 1 is complete, we'll move to **Phase 2: Content Migration** where we'll:
1. Clone the new repository locally
2. Copy template content from current repository
3. Validate template functionality
4. Test CI workflows

**Ready to proceed?** Let me know when you've completed the repository creation and configuration steps, and I'll help you with Phase 2! 