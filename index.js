addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

/**
 * Fetch and log a request
 * @param {Request} request
 */

async function rawHtmlResponse(html) {
  const init = {
    headers: {
      "content-type": "text/html;charset=UTF-8"
    }
  };

  return new Response(html, init);
}

async function handleRequest(request) {
  console.log('Got request', request)
  const response = await fetch(request)
  console.log('Got response', response)
  const getCache = () => pages.get('index');
  const page = await getCache();
  return rawHtmlResponse(page)
}

