"use client";

import {
  Dialog,
  DialogTrigger,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
} from "@/components/ui/dialog";
import { BrainCircuit } from "lucide-react";
import { useState } from "react";
import { PREDICT_PARKING } from "@/lib/api";
import { parseISO } from "date-fns";
import { apolloClient } from "@/lib/utils";

export function PredictionDialog() {
  const [predictedOccupancy, setPredictedOccupancy] = useState<
    String | undefined
  >(undefined);
  const [selectedDate, setSelectedDate] = useState<string>("") ?? "";

  const handlePredict = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const { data } = await apolloClient.mutate({
      mutation: PREDICT_PARKING,
      variables: { datetime: parseISO(selectedDate) },
    });
    setPredictedOccupancy(data?.predictParking);
  };

  return (
    <Dialog>
      <DialogTrigger asChild>
        <button className="bg-cyan-700 rounded w-12 h-12 flex items-center justify-center px-3">
          <BrainCircuit color="white" size={24} />
        </button>
      </DialogTrigger>
      <DialogContent className="bg-white">
        <DialogHeader>
          <DialogTitle>Predict Parking Occupancy</DialogTitle>
          <DialogDescription>
            Select a date to predict parking occupancy.
          </DialogDescription>
        </DialogHeader>
        <form onSubmit={handlePredict} className="mt-4">
          <label
            htmlFor="date"
            className="block text-sm font-medium text-gray-700"
          >
            Date:
          </label>
          <input
            type="datetime-local"
            id="date"
            name="date"
            value={selectedDate}
            onChange={(e) => setSelectedDate(e.target.value)}
            required
            className="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-cyan-500 focus:border-cyan-500"
          />
          <button
            type="submit"
            className="mt-4 w-full bg-sky-800 text-white py-2 rounded-md hover:bg-sky-700 focus:outline-none focus:ring-2 focus:ring-sky-500"
          >
            Predict
          </button>
        </form>
        {predictedOccupancy && (
          <div className="mt-6 text-center">
            <p className="text-lg font-semibold text-gray-800">
              Predicted Occupancy: {predictedOccupancy} Cars
            </p>
          </div>
        )}
      </DialogContent>
    </Dialog>
  );
}
