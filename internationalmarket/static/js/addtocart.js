var updatebuttons = document.getElementsByClassName('update-cart')

for(var i = 0; i < updatebuttons.length; i++){
    updatebuttons[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)
        console.log('user:', user)

    })
}