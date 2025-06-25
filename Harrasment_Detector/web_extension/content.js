function scanText() {
  let comments = document.querySelectorAll("p, span, div");
  
  comments.forEach(comment => {
    let text = comment.innerText;
    
    chrome.runtime.sendMessage({ action: "analyzeText", text }, response => {
      if (response && response.category) {
        let color = response.category === "High" ? "red" : response.category === "Medium" ? "orange" : "green";
        comment.style.border = `2px solid ${color}`;
        comment.title = `Harassment Level: ${response.category}`;
      }
    });
  });
}

// Run on page load
scanText();

