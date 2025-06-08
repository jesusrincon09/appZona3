document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'dayGridMonth',
      locale: 'es',
      noEventsText: 'No hay eventos para mostrar',
      allDayText: 'Todo el día',
      eventColor: '#2a2f5b', 
      eventTextColor: 'white',
      headerToolbar: {
        left: 'prev,next',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
      },
      buttonText: {
        dayGridMonth: 'Mes',
        timeGridWeek: 'Semana',
        timeGridDay: 'Día',
        listWeek: 'Lista'
      },slotLabelFormat: {
        hour: 'numeric',
        minute: '2-digit',
        meridiem: 'short',
        hour12: true 
      },
      eventTimeFormat: {
        hour: 'numeric',
        minute: '2-digit',
        meridiem: 'short',
        hour12: true 
      },
      events:'/reservations/',
      eventClick: function(info) {
        const props = info.event.extendedProps;

        document.getElementById('clientName').textContent = props.client_name || info.event.title;
        document.getElementById('clientCell').textContent = props.client_cell || '';
        document.getElementById('clientEmail').textContent = props.client_email || '';
        document.getElementById('spaceName').textContent = props.space || '';
        document.getElementById('reservationStart').textContent = info.event.start
       document.getElementById('reservationStart').textContent = info.event.start
          ? info.event.start.toLocaleString('es-ES', {
              day: 'numeric',
              month: 'long',
              year: 'numeric',
              hour: 'numeric',
              minute: '2-digit',
              hour12: true
            })
          : '';

        document.getElementById('reservationEnd').textContent = info.event.end
          ? info.event.end.toLocaleString('es-ES', {
              day: 'numeric',
              month: 'long',
              year: 'numeric',
              hour: 'numeric',
              minute: '2-digit',
              hour12: true
            })
          : '';


        var modal = new bootstrap.Modal(document.getElementById('reservationModal'));
        modal.show();
      },
    datesSet: function(info) {
        const month = info.start.toLocaleString('es-ES', { month: 'long' });
        const year = info.start.getFullYear();
        const customTitle = `Reservas ${month} de ${year}`;
        const titleEl = calendarEl.querySelector('.fc-toolbar-title');
        if (titleEl) {
            titleEl.textContent = customTitle;
        }
    }
    });
    calendar.render();
  });