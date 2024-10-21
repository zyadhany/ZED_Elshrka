function startTimer(days, hours, minutes, display) {
    timerDisplay = document.getElementById("timerDisplay");
    let totalSeconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60);
    let timer = totalSeconds, seconds;
    const oneSecond = 1000;

    const countdownInterval = setInterval(function () {
        hours = Math.floor(timer / 3600);
        minutes = Math.floor((timer % 3600) / 60);
        seconds = Math.floor(timer % 60);

        hours = hours < 10 ? "0" + hours : hours;
        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = hours + ":" + minutes + ":" + seconds;

        if (--timer < 0) {
            clearInterval(countdownInterval);
            display.textContent = "00:00:00";
            // Display modal
            const modal = document.querySelector('.modal');
            modal.style.display = 'flex';
        }
    }, oneSecond);
}

// Start the timer when the page loads
window.onload = function () {
    const days = 2;
    const hours = 0;
    const minutes = 0;
    startTimer(days, hours, minutes, timerDisplay);
};