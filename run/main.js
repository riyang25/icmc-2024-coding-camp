const query = new URLSearchParams(window.location.search);
const progIDs = new Set(["0", "1", "2", "3", "4", "5"]);

(async function () {
    let progID = query.get("progid");
    if (progID === null || !progIDs.has(progID)) {
        progID = "0";
    }
    let progResponse = await fetch(`./data/${progID}.txt`);

    // Wrangle encodings to work.
    let progBase64 = await progResponse.text();
    let progAscii = atob(progBase64);
    let progBytes = new Uint8Array(progAscii.length);
    for (let i = 0; i < progAscii.length; ++i) {
        progBytes[i] = progAscii.charCodeAt(i);
    }
    let prog = new TextDecoder('utf-8').decode(progBytes);

    // Work around weird bug in Pyscript.
    // Previously printed lines are duplicated by an input with an empty string.
    prog = prog.replace(new RegExp("input\\(\\)", "g"), "input(\"> \")");

    document.body.innerHTML += `
<script id="python-script" type="py" terminal worker>
${prog}
print("Program exited successfully.")
</script>
`
})();
