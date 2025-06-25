chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "analyzeText") {
    fetch("http://127.0.0.1:8000/classify", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: message.text })
    })
    .then(response => response.json())
    .then(data => sendResponse({ category: data.category, confidence: data.confidence }))
    .catch(error => sendResponse({ error: error.toString() }));
    
    return true; // Keep the message channel open for async response
  }
});

