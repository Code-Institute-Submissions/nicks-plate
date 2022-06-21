// message log in log out to see schedule
setTimeout(function() {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close()
}, 3000);



// Auto scroll down 100vh from header
document.getElementById("scroll-down").addEventListener('click', () => {
    window.scrollTo(0, window.innerHeight);
})

// add color on todays day
const d = new Date()
let day = d.getDay()
if (day == 1) {
    document.getElementById('one').style="background-color: antiquewhite;";
} else {
    document.getElementById('one').style="background-color: white;";
}
if (day == 2) {
    document.getElementById('two').style="background-color: antiquewhite;";
} else {
    document.getElementById('two').style="background-color: white;";
}
if (day == 3) {
    document.getElementById('three').style="background-color: antiquewhite;";
} else {
    document.getElementById('three').style="background-color: white;";
}
if (day == 4) {
    document.getElementById('four').style="background-color: antiquewhite;";
} else {
    document.getElementById('four').style="background-color: white;";
}
if (day == 5) {
    document.getElementById('five').style="background-color: antiquewhite;";
} else {
    document.getElementById('five').style="background-color: white;";
}
if (day == 6) {
    document.getElementById('six').style="background-color: antiquewhite;";
} else {
    document.getElementById('six').style="background-color: white;";
}
if (day == 0) {
    document.getElementById('zero').style="background-color: antiquewhite;";
} else {
    document.getElementById('zero').style="background-color: white;";
}
