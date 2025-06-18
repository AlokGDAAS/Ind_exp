import React from 'react'
import { useSelector } from 'react-redux'
import AddCard from './AddCard'
import FlashCardList from './FlashCardList'

function FlashCardGroup() {

    const groups = useSelector((state) =>state.flashcards)

    
       


  return (
    <div>
        {groups.map((group)=>(

            <div key={group.id} style={{border:"1px solid gray", padding:"10px", margin:"10px"}}>
                <h2>{group.title}</h2>
                <AddCard groupId={group.id}/>
                <FlashCardList cards={group.cards}/>
                

            </div>

        ))}
       

    </div>
  )
}

export default FlashCardGroup