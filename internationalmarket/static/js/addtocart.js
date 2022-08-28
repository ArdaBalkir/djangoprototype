var updatebuttons = document.getElementsByClassName('update-cart')

for(var i = 0; i < updatebuttons.length; i++){
    updatebuttons[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)
        console.log('user:', user)
        
        if (user === 'AnonymousUser'){
            console.log('User not logged in')
        }else{
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log('User is authenticated')
    var url = '/update_item/'

    fetch(url, {
        method : 'POST',
        headers : {
            'Content-Type':'application/json',
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })

    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}
