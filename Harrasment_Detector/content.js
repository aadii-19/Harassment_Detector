document.addEventListener("input", function (event) {
    let inputFields = document.querySelectorAll("textarea, input[type='text']");
    inputFields.forEach((field) => {
        field.addEventListener("change", async () => {
            let text = field.value;
            let response = await fetch("http://127.0.0.1:8000/analyze", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: text })
            });
            let result = await response.json();
            if (result.is_harassment) {
                alert("⚠️ Harassment detected! This message may be flagged.");
                field.style.border = "2px solid red"; // Highlight input field
                chrome.runtime.sendMessage({ text: text }); // Send to background script for admin alert
            }
        });
    });
});
