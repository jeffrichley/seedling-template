> "Code is like humor. When you have to explain it, it’s bad."
> — **Cory House**

# 🌱 Seedling Pull Request Checklist

Hello, brave contributor! 👋  Please fill out the sections below so reviewers (human *and* automated) can glide through your changes without spelunking the diff.

---

## ✍️ Description

Briefly summarize **what** this PR does **and** *why* it matters. Link any related issues.

```
Fixes #<issue‑number>
Closes #<issue‑number>
```

---

## 📦 Type of Change *(tick all that apply)*

* [ ] 🐛 **Bug fix** – non‑breaking patch
* [ ] ✨ **New feature** – shiny but non‑breaking
* [ ] 💥 **Breaking change** – existing behaviour altered
* [ ] 📝 **Docs** – documentation‑only update
* [ ] ♻️ **Refactor / chore** – code cleanup, build tooling, etc.

---

## 🧪 How Has This Been Tested?

Explain the tests you ran (or added) to verify your changes.

```markdown
- [ ] Unit tests (`pytest -k name`)
- [ ] Integration tests (`nox -s tests-integration`)
- [ ] Manual QA (describe steps):
      1. …
      2. …
```

---

## ✅ Checklist *(keep it honest)*

* [ ] My code follows the project’s style guidelines 🧹
* [ ] I performed a self‑review of my changes 💭
* [ ] I commented the hard‑to‑grok parts 💬
* [ ] I updated **docs** where relevant 📚
* [ ] My changes produce **no new warnings** 🚫
* [ ] I added **tests** that cover my changes 🧪
* [ ] Existing tests **all pass** locally ✅
* [ ] Dependent changes (if any) are merged & published 🔗

> 💡 **Tip:** Run `just pr-check` before requesting review — it lints, types, and tests in one go.
