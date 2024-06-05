document.addEventListener('DOMContentLoaded', function() {
    let table = new DataTable('#myTable', {
        // options
        searchable: true,
    });

    // Use event delegation to handle clicks on screen rows
    document.querySelector('#myTable tbody').addEventListener('click', function(event) {
        if (event.target && event.target.closest('tr.screen-row')) {
            var row = event.target.closest('tr.screen-row');
            var screenId = row.dataset.screenId;
            var screenName = row.dataset.screenName;

            showForm(screenId, screenName);
        }
    });
});

function showForm(screenId, screenName) {
    console.log('Screen ID:', screenId);
    console.log('Screen Name:', screenName);
    var formHTML = `<h4>Options for ${screenName}</h4>
                    <button onclick="editScreenName('${screenId}', '${screenName}')" class="btn btn-secondary mt-2">Edit Name</button>
                    <button onclick="editScreenFields('${screenId}')" class="btn btn-secondary mt-2">Edit Fields</button>
                    <button onclick="copyScreen('${screenName}')" class="btn btn-primary mt-2">Copy</button>`;
    document.getElementById('form_area').innerHTML = formHTML;
}

function editScreenName(screenId, screenName) {
    var newName = prompt('Enter the new screen name:', screenName);
    console.log('New Name:', newName);
    if (newName && newName !== screenName) {
        fetch(`/edit_screen_name`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name: newName, screenId: screenId})
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            if (data.status === 'success') {
                alert('Screen name updated successfully!');
                screenName = newName;
                location.reload();
            } else {
                alert(`Error: ${data.message}`);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Failed to update screen name.');
        });
    }
}

function editScreenFields(screenId) {
    // Implement your logic to edit screen fields
    alert('Edit Fields functionality to be implemented.');
}

function copyScreen(originalScreenName) {
    var newScreenName = prompt('Enter the new screen name:');
    if (newScreenName) {
        const body = {
            originalScreenName: originalScreenName,
            newScreen: newScreenName
        };

        fetch('/copy_screen', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert(`Screen copied successfully! New screen ID: ${data.id}`);
                location.reload();
            } else {
                alert(`Error: ${data.message}`);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Failed to copy screen.');
        });
    }
}


//#region API Endpoints
// https://dev.instance-name/rest/scriptrunner/latest/custom/copyScreen
// Method: POST
// {
//     "originalScreen": "TEAH: CLOSED - 1",
//     "newScreen": "TEAH: CLOSED - TEST 2"
//   }
//#endregion  
