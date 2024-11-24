import { createFileRoute } from "@tanstack/react-router";
import { GET_PARKING } from "@/lib/api";
import { useQuery } from "@apollo/client";
import SimpleNav from "@/components/SimpleNav";
import { HistoricEventsChart } from "@/components/HistoricEventsChart";
import { format, parseISO } from "date-fns";
import { ParkingEntry } from "@/__generated__/graphql";

export const Route = createFileRoute("/parking/$identifier")({
  component: RouteComponent,
});

function RouteComponent() {
  const { identifier } = Route.useParams();
  const { data } = useQuery(GET_PARKING, {
    variables: { identifier: identifier },
  });

  const entries = data?.parking?.entries || [];

  const sortedEntries = [...entries]
    .sort(
      (a, b) =>
        parseISO(b?.createdAt).getTime() - parseISO(a?.createdAt).getTime()
    )
    .slice(0, 20);

  return (
    <div className="flex flex-col h-screen w-full bg-sky-100">
      <SimpleNav disabledParkingTab={true} activeTab='parking' />
      <div className="h-full w-full flex flex-col items-center">
        <div className="bg-white w-full h-[30rem] flex py-5">
          <div className="m-auto">
            <div className="mr-auto ml-auto w-min flex gap-5">
              <span className="text-sky-800 text-5xl w-full text-center font-bold mb-4">
                Occupied
              </span>
              <div className="bg-sky-800 rounded-3xl p-2 w-min h-min">
                <span className="text-white text-3xl">
                  {data?.parking?.occupiedLots}/{data?.parking?.totalLots}
                </span>
              </div>
            </div>
            <img
              src="/parking_header.png"
              alt="Parking Header"
              className="mr-auto ml-auto"
            />
          </div>
        </div>
        {(data?.parking?.entries?.length ?? 0 > 0) ? (
          <div className="flex h-max w-full p-10 flex-col bg-sky-700">
            <span className="text-white text-5xl w-full text-center font-semibold mb-4">
              Historic
            </span>
            <HistoricEventsChart
              data={
                data?.parking?.entries?.filter(
                  (entry): entry is ParkingEntry => entry != null
                ) || []
              }
            />

            <span className="text-white text-5xl w-full text-center font-semibold mb-4 mt-10">
              Last Entrys
            </span>
            <div className="mr-auto ml-auto max-w-[60rem] w-full rounded-3xl bg-white h-max py-5">
              {sortedEntries.map((e) => {
                const dateObject = parseISO(e?.createdAt);
                return (
                  <div
                    key={e?.createdAt}
                    className="flex items-center w-full mx-5 mr-10 ml-5"
                  >
                    <span className="text-left font-semibold text-sky-700">
                      {e?.entryType}
                    </span>
                    <div className="flex-grow border-t border-dashed border-sky-700"></div>
                    <span className="text-right mr-10 font-semibold text-sky-700">
                      {format(dateObject, "HH:mm")}
                    </span>
                  </div>
                );
              })}
            </div>
          </div>
        ) : (
          <div className="flex h-screen w-full p-10 flex-col bg-sky-700">
            <span className="text-white text-5xl w-full text-center font-semibold mb-4">
              No data yet
            </span>
          </div>
        )}
      </div>
    </div>
  );
}

export default RouteComponent;
