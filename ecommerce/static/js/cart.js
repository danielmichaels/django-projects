let updateBtns = document.getElementsByClassName('update-cart')

function updateUserOrder(productId, action) {
    console.log(`${user} authenticated, sending data of ${productId}:${action}`)

    let url = '/update_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })
        .then((resp) => {
            return resp.json()
        })
        .then((data) => {
            location.reload()
        })
}

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        let productId = this.dataset.product
        let action = this.dataset.action
        console.log(`productId: ${productId} - Action: ${action}`)

        console.log(`USER: ${user}`)
        if (user === 'AnonymousUser') {
            console.log('not auth')
        } else {
            updateUserOrder(productId, action)
        }
    })
}
