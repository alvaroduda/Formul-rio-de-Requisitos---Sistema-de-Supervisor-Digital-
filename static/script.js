document.addEventListener('DOMContentLoaded', function() {
    
    const form = document.getElementById('requisitosForm');
    const disponibilidadeRadios = document.querySelectorAll('input[name="disponibilidade"]');
    const horariosField = document.getElementById('horariosField');
    const submitBtn = document.querySelector('.btn-submit');
    const resetBtn = document.querySelector('.btn-reset');

    
    function toggleHorariosField() {
        const horariosProgramados = document.querySelector('input[name="disponibilidade"][value="Horários programados"]');
        
        if (horariosProgramados && horariosProgramados.checked) {
            horariosField.style.display = 'block';
            
            const horariosInput = document.getElementById('horarios');
            if (!horariosInput.value.trim()) {
                horariosInput.value = '10h e 16h (padrão)';
            }
        } else {
            horariosField.style.display = 'none';
            
            document.getElementById('horarios').value = '';
        }
    }

    
    disponibilidadeRadios.forEach(radio => {
        radio.addEventListener('change', toggleHorariosField);
    });

    
    function validateField(field) {
        const value = field.value.trim();
        
        
        field.style.borderColor = '#e5e7eb';
        field.style.backgroundColor = '#f9fafb';
        return true;
    }

    
    function validateRadioGroup(groupName) {
        const radios = document.querySelectorAll(`input[name="${groupName}"]`);
        const isChecked = Array.from(radios).some(radio => radio.checked);
        
        radios.forEach(radio => {
            const label = radio.closest('.radio-label');
            
            label.style.borderColor = '#e5e7eb';
            label.style.backgroundColor = '#f9fafb';
        });
        
        return true; 
    }

    
    const textInputs = document.querySelectorAll('input[type="text"], textarea');
    textInputs.forEach(input => {
        input.addEventListener('blur', () => validateField(input));
        input.addEventListener('input', () => {
            if (input.style.borderColor === 'rgb(239, 68, 68)') {
                validateField(input);
            }
        });
    });

    
    const radioGroups = ['disponibilidade', 'registro', 'hospedagem', 'email_config'];
    radioGroups.forEach(groupName => {
        const radios = document.querySelectorAll(`input[name="${groupName}"]`);
        radios.forEach(radio => {
            radio.addEventListener('change', () => validateRadioGroup(groupName));
        });
    });

    
    function validateForm() {
        
        return true;
    }

    
    function showLoading() {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span>⏳ Enviando...</span>';
    }

    
    function hideLoading() {
        submitBtn.disabled = false;
        submitBtn.innerHTML = '<span>📤 Enviar Formulário</span>';
    }

    
    form.addEventListener('submit', function(e) {
        
        showLoading();
    });

   
    resetBtn.addEventListener('click', function() {
        if (confirm('Tem certeza que deseja limpar todos os campos do formulário?')) {
            form.reset();
            horariosField.style.display = 'none';
            
            
            textInputs.forEach(input => {
                input.style.borderColor = '#e5e7eb';
                input.style.backgroundColor = '#f9fafb';
            });
            
            document.querySelectorAll('.radio-label').forEach(label => {
                label.style.borderColor = '#e5e7eb';
                label.style.backgroundColor = '#f9fafb';
            });
            
            showNotification('Formulário limpo com sucesso!', 'success');
        }
    });

    
    function showNotification(message, type) {
        
        const existingNotifications = document.querySelectorAll('.notification');
        existingNotifications.forEach(notification => notification.remove());
        
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.innerHTML = `
            <span>${type === 'success' ? '✅' : '❌'}</span>
            <span>${message}</span>
        `;
        
        
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px 20px;
            border-radius: 10px;
            color: white;
            font-weight: 500;
            z-index: 1000;
            display: flex;
            align-items: center;
            gap: 10px;
            max-width: 400px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            animation: slideInRight 0.3s ease;
            ${type === 'success' ? 
                'background: linear-gradient(135deg, #10b981 0%, #059669 100%);' : 
                'background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);'
            }
        `;
        
        document.body.appendChild(notification);
        
        
        setTimeout(() => {
            notification.style.animation = 'slideOutRight 0.3s ease';
            setTimeout(() => notification.remove(), 300);
        }, 5000);
    }

    
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideInRight {
            from {
                transform: translateX(100%);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
        
        @keyframes slideOutRight {
            from {
                transform: translateX(0);
                opacity: 1;
            }
            to {
                transform: translateX(100%);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);

    
    function saveFormData() {
        const formData = new FormData(form);
        const data = {};
        
        for (let [key, value] of formData.entries()) {
            data[key] = value;
        }
        
        localStorage.setItem('formularioRequisitos', JSON.stringify(data));
    }

    function loadFormData() {
        const savedData = localStorage.getItem('formularioRequisitos');
        if (savedData) {
            try {
                const data = JSON.parse(savedData);
                
                
                Object.keys(data).forEach(key => {
                    const field = document.querySelector(`[name="${key}"]`);
                    if (field && (field.type === 'text' || field.tagName === 'TEXTAREA')) {
                        field.value = data[key];
                    }
                });
                
                
                Object.keys(data).forEach(key => {
                    const radio = document.querySelector(`input[name="${key}"][value="${data[key]}"]`);
                    if (radio) {
                        radio.checked = true;
                    }
                });
                
                
                toggleHorariosField();
                
                showNotification('Dados do formulário restaurados automaticamente.', 'success');
            } catch (e) {
                console.error('Erro ao carregar dados salvos:', e);
            }
        }
    }

    
    form.addEventListener('input', saveFormData);
    form.addEventListener('change', saveFormData);

    
    loadFormData();

    
    window.addEventListener('beforeunload', function() {
        if (document.querySelector('.flash-success')) {
            localStorage.removeItem('formularioRequisitos');
        }
    });

    
    toggleHorariosField();
});
