"use client";

import { CartesianGrid, Line, LineChart, XAxis, YAxis } from "recharts";

import { Card, CardContent } from "@/components/ui/card";
import {
  ChartConfig,
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
} from "@/components/ui/chart";
import { ParkingEntry } from "@/__generated__/graphql";

const chartConfig = {
  count: {
    label: "Occupied",
    color: "rgb(3 105 161)",
  },
} satisfies ChartConfig;

type HistoricEventsChartProps = {
  data: ParkingEntry[];
};

export function HistoricEventsChart({ data }: HistoricEventsChartProps) {
  const formattedData = Object.groupBy(data, (entry) => {
    const date = new Date(entry.createdAt);
    date.setMinutes(0, 0, 0);
    const adjustedDate = date.toISOString().replace("T", " ").slice(0, 19);
    return adjustedDate;
  });

  const result = Object.entries(formattedData).map(([date, entries]) => ({
    date: date.slice(0, 13),
    count: entries?.length,
  }));

  return (
    <Card className="mr-auto ml-auto max-w-[60rem] w-full rounded-3xl bg-white h-max">
      <CardContent>
        <ChartContainer config={chartConfig}>
          <LineChart
            accessibilityLayer
            data={result}
            margin={{
              left: 12,
              right: 12,
            }}
          >
            <CartesianGrid vertical={false} />
            <XAxis
              dataKey="date"
              tickLine={false}
              axisLine={false}
              tickMargin={8}
            />
            <YAxis
              tickLine={false}
              axisLine={false}
              tickMargin={8}
              tickCount={3}
              domain={[0, (max: number) => Math.ceil(max * 1.1)]}
            />

            <ChartTooltip
              cursor={false}
              content={<ChartTooltipContent hideLabel />}
            />
            <Line
              dataKey="count"
              type="natural"
              stroke="rgb(3 105 161)"
              strokeWidth={2}
              dot={{
                fill: "rgb(3 105 161)",
              }}
              activeDot={{
                r: 6,
              }}
            />
          </LineChart>
        </ChartContainer>
      </CardContent>
    </Card>
  );
}
