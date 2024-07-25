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
    let progContent = new TextDecoder('utf-8').decode(progBytes);

    let prog = progContent;
    // Work around weird bug in Pyscript.
    // Previously printed lines are duplicated by an input 
    // with an empty string or contains newlines.
    // let prog = "";
    // let progLines = progContent.split("\n");
    // progLines.forEach(line => {
    //     if (line.includes("input(")) {
    //         prog += line.replace(/\\n"\)/g, "\\n> \")");
    //     } else {
    //         prog += line;
    //     }
    //     prog += "\n";
    // });
    // prog = prog.replace(/input\(\)/g, "input(\"> \")");
    // console.log(prog);

    // cowsay module required for one group.
    document.body.innerHTML += `
<script id="python-script" type="py" config='{"packages":["cowsay"]}' terminal worker>
# Work around weird bug in Pyscript.
# Previously printed lines are duplicated by an input 
# with an empty string or contains newlines.
_original_input_ = input
def input(prompt: str = ""):
    print(prompt, end="")
    if not prompt or prompt.endswith("\\n"):
        return _original_input_("> ")
    return _original_input_()
${prog}
print("Program exited successfully.")
</script>
`
})();
