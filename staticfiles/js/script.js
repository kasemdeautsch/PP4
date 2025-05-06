const editButtons = document.getElementsByClassName('btn-edit');
const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
const deleteButtons = document.getElementsByClassName('btn-delete');
const deleteConfirm = document.getElementById('deleteConfirm');
/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated reservation's ID upon click.
* - Updates the `button` link's href to point to the 
*   editing endpoint for the specific reservation.
*/
for(let button of editButtons){
    button.addEventListener("click", (e) => {
        let reservationId=e.target.getAttribute('data-reserv_id');
        button.href= `edit_reservation/${reservationId}`;
    });
}
/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated reservation's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
*   deletion endpoint for the specific reservation.
* - Displays a confirmation modal (`deleteModal`) to prompt 
*   the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener('click', (e) => {
        let reservationId= e.target.getAttribute('data-reserv_id');
        deleteConfirm.href = `delete_reservation/${reservationId}`;
        deleteModal.show();
    });
}