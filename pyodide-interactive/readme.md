# worker-pyodide-console
Sourced from https://github.com/hoodmane/worker-pyodide-console.  
Initially, the intent was to use this project to provide a Python console environment,  
but Pyscript turned out to fit that use case more appropriately.  
Regardless, it's nice to have here anyways.

## Modifications
- Updated the CDN URL in `pyodide-worker.js`.
- Added `sw.js` from https://github.com/ArthurSonzogni/FTXUI/blob/main/examples/sw.js.
- Updated `index.html` to load `sw.js`.
- Updated `pyodide-main.js` to use the fetch API to load the web worker.
- Updated the way `pyodide-worker.js` fetches `console_main.py`.
- Updated Pyodide to `0.26.1`.
