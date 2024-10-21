
function startTimer(totalSeconds, display) {
    timerDisplay = document.getElementById("timerDisplay");
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

        if (timer-- < 0) {
            clearInterval(countdownInterval);
            display.textContent = "00:00:00";
            alert('Contest has started');
            location.reload();
        }
    }, oneSecond);
}
