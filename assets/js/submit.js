function handleFileSelect(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('code').value = e.target.result;
        };
        reader.readAsText(file);
    }
}

function handleSubmit(event) {
    event.preventDefault();
    
    const teamName = document.getElementById('team_name').value;
    const code = document.getElementById('code').value;
    
    if (!code) {
        showMessage('Molimo vas da unesete kod ili otpremite fajl', 'error');
        return;
    }

    // Since we can't process the submission server-side with GitHub Pages,
    // we'll show a success message and provide instructions
    showMessage(`Primljena prijava od tima: ${teamName}\n` +
               'Molimo vas da kod pošaljete putem GitHub Issues na repozitorijumu.', 'success');
    
    // Optional: Open GitHub Issues in new tab
    window.open('https://github.com/njaric03/PrisonersDillemaTournament/issues/new', '_blank');
}

function showMessage(text, type) {
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = text;
    messageDiv.style.display = 'block';
    messageDiv.className = `message ${type}`;
}
