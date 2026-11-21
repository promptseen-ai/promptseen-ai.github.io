# SEO management checklist

## Static-site SEO configuration
- SEO metadata is maintained directly in HTML because this project is hosted as static GitHub Pages content (no WordPress runtime/plugin support).
- One primary SEO metadata implementation per page: title, meta description, canonical, robots, Open Graph, X/Twitter cards, and JSON-LD.
- Homepage schema: WebSite and Organization.
- Article schema: Article + BreadcrumbList, with a generic organization publisher/author, not personal identity.
- XML sitemap at /sitemap.xml; robots file points to it.
- llms.txt offers a short, factual site map for AI crawlers.
- Keep canonical host consistent with GitHub Pages URL.

## Every new article
1. Confirm keyword/topic intent and avoid targeting the exact same intent as another article.
2. Write an original title (ideally descriptive; avoid fake trend claims) and unique meta description.
3. Add canonical URL and index/follow robots directive.
4. Use one clear H1; organize with descriptive H2/H3; no heading keyword stuffing.
5. Provide original prompts and helpful instructions; avoid copying competitors' text or images.
6. Add relevant internal links to homepage categories and sibling articles.
7. Add Article schema and BreadcrumbList; dates must be real, not invented.
8. Add the article URL to sitemap.xml; update robots only if site rules change.
9. Review mobile layout, readability, copy buttons, accessibility labels and broken links.
10. Check deployment and HTTP response before marking live.

## Technical SEO maintenance
- Keep sitemap limited to canonical, indexable pages that return 200.
- Use noindex only on pages intentionally excluded from search.
- Avoid duplicate titles/descriptions and duplicate schema blocks.
- Don't create empty category pages or doorway pages.
- Search Console and Bing Webmaster verification require account-specific verification tokens; don't invent them.
- Ranking, impressions and indexing are not guaranteed.

## Current setup limitations
- GitHub Pages is a static host, so Yoast SEO or Rank Math WordPress plugins cannot be installed here. Equivalent technical features are added as code and checked by CI.
- Google Search Console and Bing Webmaster Tools have not been connected; property verification and sitemap submission require owner access.
- Live deployment and index status should be verified after GitHub Pages deployment.

## Current tracked pages
- Homepage: https://promptseen-ai.github.io/
- Article: https://promptseen-ai.github.io/articles/gemini-ai-photo-editing-prompts-for-boys.html
