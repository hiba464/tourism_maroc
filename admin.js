async function loadReservations() {

    const response =
        await fetch(
            "http://127.0.0.1:5000/admin/reservations"
        );

    const reservations =
        await response.json();

    const table =
        document.getElementById(
            "reservationsTable"
        );

    table.innerHTML = "";

    reservations.forEach(r => {
       table.innerHTML += `

<tr>

    <td>${r.id}</td>

    <td>${r.full_name}</td>

    <td>${r.email}</td>

    <td>${r.hotel_name}</td>

    <td>${r.check_in}</td>

    <td>${r.check_out}</td>

    <td>${r.guests}</td>

    <td>

        <button
        onclick="deleteReservation(${r.id})"
        >
            Delete
        </button>

    </td>

</tr>

`;
       
        

    });

}

async function loadStats(){

    const response =
        await fetch(
            "http://127.0.0.1:5000/admin/stats"
        );

    const data =
        await response.json();

    document.getElementById(
        "usersCount"
    ).innerText =
    data.users;

    document.getElementById(
        "reservationsCount"
    ).innerText =
    data.reservations;

    document.getElementById(
        "reviewsCount"
    ).innerText =
    data.reviews;

    document.getElementById(
        "hotelsCount"
    ).innerText =
    data.hotels;
}

loadStats();
loadReservations(); 



async function deleteReservation(id){

    if(
        !confirm(
            "Delete Reservation ?"
        )
    ){
        return;
    }

    await fetch(
        `http://127.0.0.1:5000/admin/delete_reservation/${id}`,
        {
            method:"DELETE"
        }
    );

    loadReservations();
    loadStats();
}
