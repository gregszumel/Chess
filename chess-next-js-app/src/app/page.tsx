"use client";

import { useDrag, DragPreviewImage, DndProvider } from "react-dnd";
import { FC } from "react";
import knight from "./Chess_KnightDark.svg";
import { HTML5Backend } from "react-dnd-html5-backend";

const ItemTypes = { KNIGHT: "knight" };

export default function Home() {
  return (
    <DndProvider backend={HTML5Backend}>
      <div className="h-full">
        Name 1: Score
        <div className="flex">
          <Knight />
          <Board />
          <div> MovesList</div>
        </div>
        Name 2: Score
      </div>
    </DndProvider>
  );
}

const Knight: FC = () => {
  const [{ isDragging }, drag, preview] = useDrag(
    () => ({
      type: ItemTypes.KNIGHT,
      collect: (monitor) => ({
        isDragging: !!monitor.isDragging(),
      }),
    }),
    []
  );

  return (
    <>
      <div
        ref={drag}
        style={{
          opacity: isDragging ? 0.5 : 1,
          fontSize: 25,
          fontWeight: "bold",
          cursor: "move",
        }}
      >
        ♘
      </div>
      ,
    </>
  );
};

function Board() {
  const rows = [];
  for (let i = 0; i < 8; i++) {
    rows.push(<Row isEven={i % 2 == 0} />);
  }
  return <div>{rows}</div>;
}

function Row({ isEven }: { isEven: boolean }) {
  const row = [];
  for (let i = 0; i < 8; i++) {
    row.push(<Square color={(i + +isEven) % 2 == 0 ? "white" : "black"} />);
  }
  return <div className="flex ">{row}</div>;
}

function Square({ color }: { color: string }) {
  const cn =
    color === "white"
      ? "border w-28 h-28 bg-gray-600"
      : "border w-28 h-28 bg-gray-900";
  console.log(cn);
  return <div className={cn}></div>;
}
