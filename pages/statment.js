function submitCode() {
    var code = document.getElementById('code').value;
    
    // Send code to backend for processing (you need to implement this part)
    
    // For demonstration, let's just display the code in the output
    document.getElementById('output').innerHTML = '<pre>' + code + '</pre>';
}
