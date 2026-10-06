// My first Azure infrastructure
param location string = 'southafricanorth'
param vmName string = 'myFirstVM'

resource vnet 'Microsoft.Network/virtualNetworks@2023-04-01' = {
  name: 'myVnet'
  location: location
  properties: {
    addressSpace: {
      addressPrefixes: ['10.0.0.0/16']
    }
  }
}

output vnetId string = vnet.id
