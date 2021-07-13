$(document).ready(function() {
    $('#table_id').DataTable({
        responsive: true,
        dom: 'Bfrtip',
        buttons: [
            'excel'
        ],
        drawCallback: function() {
            var api = this.api();
            $("#salary").html(api.column(3, { page: 'current' }).data().sum());
        }
    });
});