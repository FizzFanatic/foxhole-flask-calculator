
window.onload = function() {
        // Отримуємо елемент з id "results"
        var resultsElement = document.getElementById("results");

        // Перевіряємо, чи існує цей елемент
        if (resultsElement) {
            // Прокручуємо сторінку до елемента з id "results" з плавною анімацією
            resultsElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }

        // Отримуємо всі елементи з класом "error-message"
        var errorMessages = document.getElementsByClassName("error-message");

        // Перевіряємо, чи є хоча б один елемент із повідомленням про помилку
        if (errorMessages.length > 0) {
            // Отримуємо перший елемент із помилкою
            var firstErrorMessage = errorMessages[0];

            // Прокручуємо сторінку до першого елементу з помилкою з плавною анімацією
            firstErrorMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    };