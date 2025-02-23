document.addEventListener("DOMContentLoaded", function() {
    let startPicker = flatpickr("#id_reservation_start", {
        enableTime: true,
        dateFormat: "d-m-Y h:i K",
        time_24hr: false,
        minuteIncrement: 1,
        minDate: "today",
        onChange: function(selectedDates, dateStr, instance) {
            let selectedDate = selectedDates[0];
            let endPickerInstance = document.querySelector("#id_reservation_end")._flatpickr;

            if (!endPickerInstance.selectedDates[0] || endPickerInstance.selectedDates[0] < selectedDate) {
                endPickerInstance.setDate(selectedDate, true);
            }

            endPickerInstance.set("minDate", selectedDate);
        }
    });

    let endPicker = flatpickr("#id_reservation_end", {
        enableTime: true,
        dateFormat: "d-m-Y h:i K",
        time_24hr: false,
        minuteIncrement: 1,
        minDate: "today",
    });

    // Botón para limpiar fecha de inicio
    document.getElementById("clear-start").addEventListener("click", function() {
        startPicker.clear();
    });

    // Botón para limpiar fecha de fin
    document.getElementById("clear-end").addEventListener("click", function() {
        endPicker.clear();
    });

    // capturar el evento submit del formulario
    document.getElementById("reservation-form").addEventListener("submit", function(event) {
        let start = startPicker.selectedDates[0];
        let end = endPicker.selectedDates[0];
        //formatear la fecha en formato ISO
        document.getElementById("id_reservation_start").value = start.toISOString();
        document.getElementById("id_reservation_end").value = end.toISOString();
    });
});