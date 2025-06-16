document.querySelectorAll(".category").forEach(button => {
    button.addEventListener("click", function(event) {
        event.preventDefault();
        document.querySelectorAll(".category").forEach(btn => btn.classList.remove("category_active"));
        this.classList.add("category_active");
        window.location.href = this.href;
    });
});

function toggleLeagues(leagueId, button) {
    let leagueList = document.getElementById(leagueId);
    let icon = button.querySelector("i"); // Отримуємо іконку стрілки

    if (leagueList.classList.contains("open")) {
        leagueList.classList.remove("open");
        icon.classList.remove("fa-angle-up");
        icon.classList.add("fa-angle-down"); // Змінюємо іконку на вниз
    } else {
        leagueList.classList.add("open");
        icon.classList.remove("fa-angle-down");
        icon.classList.add("fa-angle-up"); // Змінюємо іконку на вверх
    }
}

window.onscroll = function() {
    let scrollButton = document.getElementById("scrollTopBtn");
    if (document.documentElement.scrollTop > 100) {
        scrollButton.classList.add("show");
    } else {
        scrollButton.classList.remove("show");
    }
};

function scrollToTop() {
    window.scrollTo({ top: 0, behavior: "smooth" });
}
