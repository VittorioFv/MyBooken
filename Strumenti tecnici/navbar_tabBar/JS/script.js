const toggle = document.getElementById('toggle');
const sidebar = document.getElementById('sidebar');
const toggletoken = document.getElementById('toggletoken');
const sidebartoken = document.getElementById('sidebartoken');

document.onclick = function (e) {
    if (e.target.id !== 'toggle' && e.target.id !== 'sidebar') {
        toggle.classList.remove('active');
        sidebar.classList.remove('active');
    }
    if (e.target.id !== 'sidebartoken' && e.target.id !== 'toggletoken') {
        toggletoken.classList.remove('active');
        sidebartoken.classList.remove('active');
    }
}

toggle.onclick = function () {
    toggle.classList.toggle('active');
    sidebar.classList.toggle('active');
}

toggletoken.onclick = function () {
    toggletoken.classList.toggle('active');
    sidebartoken.classList.toggle('active');
}

