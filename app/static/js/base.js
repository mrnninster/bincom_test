// Notification Control
const controls = document.querySelectorAll('.control')
controls.forEach(control => {
    control.addEventListener('click',()=>{
        const notification = control.parentElement
        const notification_parent = notification.parentElement
        notification_parent.removeChild(notification)
    })
});