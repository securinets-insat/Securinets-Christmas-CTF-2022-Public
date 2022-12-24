//SPDX-License-Identifier: Unlicensed
pragma solidity ^0.8.0;

contract CryptoLeague {
    address public owner;
    bool fifaFunded;
    address[] players;

    constructor(address _owner) payable {
        owner = _owner;
        fifaFunded = true;
    }

    function addPlayer(address playerAddress) public payable {
        require(msg.value == 0.1 ether, "No free entries");
        players.push(playerAddress);
    }

    function deletePlayer(address playerAddress) public {
        int256 playerIndex = findPlayer(playerAddress);

        if (playerIndex > 0) {
            uint256 playerIndex = uint256(playerIndex);
            if (playerIndex < players.length - 1)
                players[playerIndex] = players[players.length - 1];
            players.pop();
        }
    }

    function findPlayer(address playerAddress) public view returns (int256) {
        for (uint256 i = 0; i < players.length; i++) {
            if (playerAddress == players[i]) return int256(i);
        }
        return -1;
    }

    function updatePlayer(uint256 index, address newAddress) public {
        players[index] = newAddress;
    }

    function clearFunds() public {
        require(msg.sender == owner, "Only owner can take the funds");
        payable(msg.sender).transfer(address(this).balance);
    }

    function isSolved() public view returns (bool) {
        return address(this).balance == 0;
    }
}
