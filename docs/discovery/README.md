# Community Notes — publishing and evidence

This is an unofficial community static page, not the official TypeSafe AI blog. Read the [README](../../README.md), [agent instructions](../../AGENTS.md), and [contribution guide](../../CONTRIBUTING.md) before editing.

## Publishing status

The site is source HTML with no confirmed production origin in this repository. Keep `og:url`, canonical, sitemap, and absolute `og:image` values unset until a host and a real raster image are chosen and verified. The current text-card metadata is intentional, not a claim that a large image preview has been deployed. Update the regression tests alongside an authorized deployment configuration change.

The [original SVG card](assets/social-preview.svg) is editable 1280×640 editorial artwork. It is not a product screenshot or an accepted GitHub raster upload by itself. Export and visually inspect a PNG before applying the separate repository Social preview setting. Follow the [shared publishing checklist](https://github.com/TypeSafeAI/.github/blob/main/docs/discovery/SHARING.md).

## Editorial guidance

Keep a stable ID and self-link for each article heading. Explain one concrete pattern with primary-source links, synthetic examples, and explicit limitations. A typed result is not proof of correctness or execution authorization. Do not add fabricated experiment results, authors, citations, testimonials, or official endorsement.

Metadata should describe the visible content. Keep titles and descriptions readable, not stuffed with unrelated trending keywords. Repository topics are capability categories, not release tags or ranking guarantees.

## Verification and screenshots

Run `python3 -m unittest discover -s tests -v`. Preview the actual HTML at desktop and narrow widths and inspect keyboard focus, article anchors, and wrapping. No external JavaScript, provider calls, credentials, or package installation is needed.

For each screenshot record the source commit/blob, viewport, capture method, and whether the page was local, preview, or production. Offline HTML renders are not deployed-site evidence. The initiative's local captures used 1440×1000 and 390×844 viewports and reported no horizontal overflow; use the exact source blob in their supplied provenance rather than treating those captures as future-build evidence.

Follow the [screenshot protocol](https://github.com/TypeSafeAI/.github/blob/main/docs/discovery/SCREENSHOTS.md). Review pixels for private content before publishing. No license or production host is established by this change.
