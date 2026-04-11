/**
 * Admin Forms Enhancements - DentiCare
 * Includes: Image Thumbnail Preview, AJAX Upload with Progress, and Cancellation.
 */

document.addEventListener('DOMContentLoaded', function() {
    initThumbnailPreview();
    initFormProgress();
});

/**
 * Handles instant image thumbnail preview for file inputs
 */
function initThumbnailPreview() {
    const fileInputs = document.querySelectorAll('input[type="file"]');
    
    fileInputs.forEach(input => {
        // Create thumbnail container if it doesn't exist
        let previewContainer = document.createElement('div');
        previewContainer.className = 'thumbnail-preview-container';
        previewContainer.innerHTML = '<img src="" alt="Preview">';
        input.parentNode.insertBefore(previewContainer, input.nextSibling);

        input.addEventListener('change', function() {
            const file = this.files[0];
            const img = previewContainer.querySelector('img');
            
            if (file && file.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    img.src = e.target.result;
                    previewContainer.style.display = 'block';
                };
                reader.readAsDataURL(file);
            } else {
                previewContainer.style.display = 'none';
            }
        });
    });
}

/**
 * Handles the form submission with a real progress bar and cancellation
 */
function initFormProgress() {
    const forms = document.querySelectorAll('.change-form form');
    const overlay = document.getElementById('admin-loading-overlay');
    const progressBar = document.getElementById('upload-progress-bar');
    const percentageText = document.getElementById('upload-percentage');
    const cancelBtn = document.getElementById('cancel-upload-btn');
    
    if (!forms.length || !overlay) return;

    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            // Only use AJAX if there are files, otherwise standard submit is fine (or faster)
            const hasFiles = form.querySelectorAll('input[type="file"]').length > 0;
            const formData = new FormData(form);
            
            // Check if user is clicking a specific save button (to keep the action)
            // Django uses the name of the button to determine the action (save, save_and_continue, etc.)
            const submitButton = e.submitter;
            if (submitButton && submitButton.name) {
                formData.append(submitButton.name, submitButton.value || '1');
            }

            e.preventDefault();
            
            const xhr = new XMLHttpRequest();
            
            // Show overlay
            overlay.style.display = 'flex';
            
            // Handle Progress
            xhr.upload.addEventListener('progress', function(e) {
                if (e.lengthComputable) {
                    const percent = Math.round((e.loaded / e.total) * 100);
                    progressBar.style.width = percent + '%';
                    percentageText.textContent = percent + '%';
                }
            });

            // Handle Completion
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4) {
                    if (xhr.status >= 200 && xhr.status < 400) {
                        // Success - Redirect or Update page based on Django's response
                        // Usually, Django redirects after a successful POST. 
                        // We can just replace the current page content or follow the redirect.
                        if (xhr.responseURL) {
                            window.location.href = xhr.responseURL;
                        } else {
                            window.location.reload();
                        }
                    } else {
                        // Error - Show error on page (this is basic, could be improved)
                        overlay.style.display = 'none';
                        const parser = new DOMParser();
                        const doc = parser.parseFromString(xhr.responseText, 'text/html');
                        const newContent = doc.querySelector('#content-main');
                        if (newContent) {
                            document.querySelector('#content-main').innerHTML = newContent.innerHTML;
                        } else {
                            alert('Erro ao salvar documento. Verifique os campos.');
                        }
                    }
                }
            };

            // Handle Cancellation
            cancelBtn.onclick = function() {
                xhr.abort();
                overlay.style.display = 'none';
                progressBar.style.width = '0%';
                percentageText.textContent = '0%';
            };

            xhr.open('POST', form.action, true);
            
            // Django CSRF is mandatory for AJAX POST
            const csrftoken = getCookie('csrftoken');
            if (csrftoken) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
            
            xhr.send(formData);
        });
    });
}

/**
 * Helper to get cookie value by name
 */
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
