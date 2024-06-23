document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript Loaded');

    // Delete Intervention Confirmation
    const deleteButtons = document.querySelectorAll('.delete-intervention-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            const interventionId = button.getAttribute('data-intervention-id');
            const interventionName = button.getAttribute('data-intervention-name');
            const confirmation = confirm(`Are you sure you want to delete the intervention "${interventionName}"?`);
            if (!confirmation) {
                event.preventDefault(); // Prevent the default action (deleting the intervention)
            }
        });
    });
});