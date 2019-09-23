# Workdown #

A system to write Markdown and have it published and hosted via [Cloudflare Workers](https://workers.cloudflare.com/)

## Pre-requisites ## 
* Python 3
* Install [`wrangler`](https://github.com/cloudflare/wrangler)

## Usage ##
1. `pip3 install workdown`
2. Run `wrangler generate site https://github.com/eldridgea/workdown-example-site`. This will generate a folder called `site` containing the folder structure `workdown` requires to work. 
3. Configure wrangler.toml with your Cloudflare details, make sure your route ends in a wildcard e.g. `route = "https://example.com/*".`
4. Create a KV Namespace and bind in to `pages` in your `wrangler.toml` file.
5. Make a markdown file ending in `.md` in the `content/` directory If you want it to be your main page, name it `index.md`.
6. From the `site` folder (or whatever you named it) run `workdown`
9. Done!

## Assets ##
Text-based assets, e.g. CSS, javascript, etc should go in the `assets/` directory. They will be available as their full filename under `assets`. For example if you make `main.css`, it will be `example.com/assets/main.css`

## Partials ##
Here is where you can customize the header and footer of pages in HTML. Currently all partials apply to all pages generated. Good things to do here would be if you have a static CSS file in `assets/` or would like to include a a fonts CDN, add it into the `<head>` in the `assets/header.html` so it will be usable on your pages. 

## Notes ##
The path for content will be the name of the markdown file with no extension. For example if you make `contact.md`, it will be `example.com/contact`.

