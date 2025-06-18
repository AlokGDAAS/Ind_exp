import React from 'react'

function FlashCardList({cards}) {
  return (
    <div>

        {cards ? cards.map((card)=>(
            <div key={card.key}>
                <p>Q. {card.question}</p>
                <p>Q. {card.answer}</p>

            </div>
        )):<h1>There is not any card</h1>}

   

    </div>
  )
}

export default FlashCardList