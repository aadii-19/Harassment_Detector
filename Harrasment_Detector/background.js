chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    fetch("http://127.0.0.1:8000/notify-admin", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: message.text })
    });
});
