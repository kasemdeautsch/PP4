console.log('Hello, project...+')

const editButtons = document.getElementsByClassName('btn-edit')

console.log(editButtons[0])

for(let button of editButtons){
    button.addEventListener('click', (e)=>{
        let reservationId=e.target.getAttribute('reserv-id')
        console.log(reservationId)
        button.href= `edit_reservation/${reservationId}`
    });
}