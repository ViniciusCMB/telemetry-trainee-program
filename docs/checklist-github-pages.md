# Checklist de Publicacao — GitHub Pages

## Antes de publicar

- [ ] `main` como branch padrao
- [ ] Workflow `deploy-gh-pages.yml` presente em `.github/workflows/`
- [ ] Docs revisados em `docs/`
- [ ] `docs/index.md` configurado como pagina inicial

## Publicacao

- [ ] Fazer commit e push para `main`
- [ ] No GitHub, ir em Settings → Pages → Source → **GitHub Actions**
- [ ] Verificar workflow rodando em Actions

## Depois de publicar

- [ ] Acessar `https://<user>.github.io/telemetry-trainee-program/docs/`
- [ ] Testar links principais e navegacao
- [ ] Corrigir links quebrados

---

> **Nota:** Este repo usa `actions/upload-pages-artifact` + `actions/deploy-pages`
> (source = **GitHub Actions**). Nao usar source = `gh-pages` branch.
