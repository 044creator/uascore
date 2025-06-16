document.querySelectorAll(".filter-btn").forEach(button => {
    button.addEventListener("click", function(event) {
        event.preventDefault();
        document.querySelectorAll(".filter-btn").forEach(btn => btn.classList.remove("active"));
        this.classList.add("active");
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll('.toggle_matches_btn');

    if (buttons.length > 0) {
        buttons.forEach(button => {
            button.addEventListener('click', function () {
                // Отримуємо унікальний ID ліги
                const leagueId = button.getAttribute('data-league-id');
                const matchesContainer = document.getElementById('matches_' + leagueId); // Знаходимо контейнер матчів за ID ліги

                if (matchesContainer) {
                    // Якщо контейнер матчів прихований
                    if (matchesContainer.style.display === "none" || !matchesContainer.style.display) {
                        matchesContainer.style.display = "block"; // Показуємо матчі
                        matchesContainer.style.height = matchesContainer.scrollHeight + "px"; // Встановлюємо висоту контейнера для анімації
                        button.classList.add('open_matches');

                        const icon = button.querySelector('i');
                        icon.classList.remove('fa-chevron-down');
                        icon.classList.add('fa-chevron-up');
                    } else {
                        matchesContainer.style.height = 0; // Приховуємо матчі
                        setTimeout(() => {
                            matchesContainer.style.display = "none"; // Точно приховуємо після анімації
                        }, 500); // Час анімації
                        button.classList.remove('open_matches');

                        const icon = button.querySelector('i');
                        icon.classList.remove('fa-chevron-up');
                        icon.classList.add('fa-chevron-down');
                    }
                }
            });
        });
    }
});


function changeDate(days) {
    let dateParts = document.getElementById("selected-date").innerText.split("/");
    let day = parseInt(dateParts[0], 10);
    let month = parseInt(dateParts[1], 10) - 1;
    let currentDate = new Date();
    currentDate.setDate(day);
    currentDate.setMonth(month);
    currentDate.setDate(currentDate.getDate() + days);
    let formattedDate = ("0" + currentDate.getDate()).slice(-2) + "/" + ("0" + (currentDate.getMonth() + 1)).slice(-2);
    window.location.href = `?date=${formattedDate}`;
}

// Функція для відправки GET запиту з урахуванням поточного шляху
function sendRequest(action) {
    const currentUrl = window.location.pathname;  // Отримуємо поточний шлях
    const url = `${currentUrl}?action=${encodeURIComponent(action)}`;  // Додаємо параметр action до поточного шляху
    window.location.href = url; // Виконуємо перехід за сформованим URL
}
// Функція для додавання/видалення класу active_button
function setActiveButton(buttonId) {
    // Знаходимо всі кнопки
    const buttons = document.querySelectorAll(".status_menu button");
    // Видаляємо клас active_button з усіх кнопок
    buttons.forEach(button => {
        button.classList.remove("active_button");
    });
    // Додаємо клас active_button лише до натиснутої кнопки
    const activeButton = document.getElementById(buttonId);
    activeButton.classList.add("active_button");
    // Зберігаємо ID активної кнопки в localStorage
    localStorage.setItem('activeButton', buttonId);
}

// Функція для відновлення активної кнопки при завантаженні сторінки
function restoreActiveButton() {
    const activeButtonId = localStorage.getItem('activeButton');
    if (activeButtonId) {
        setActiveButton(activeButtonId); // Встановлюємо активну кнопку
    }
}
// Додавання події на кнопку "Завершений"
document.getElementById("resultsButton").addEventListener("click", function() {
    setActiveButton("resultsButton"); // Додаємо активний клас
    sendRequest('Завершений');  // Параметр для завершених подій
});
// Додавання події на кнопку "Запланований"
document.getElementById("scheduledButton").addEventListener("click", function() {
    setActiveButton("scheduledButton"); // Додаємо активний клас
    sendRequest('Запланований');  // Параметр для запланованих подій
});
// Відновлення активної кнопки після перезавантаження
restoreActiveButton();