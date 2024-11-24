
"use client";

import { z } from "zod";

export const createParkingSchema = z.object({
  name: z.string().min(2, "Name must be at least 2 characters"),
  address: z.string().min(2, "Address must be at least 2 characters"),
  totalLots: z.coerce.number().min(1, "Total lots must be at least 1"),
});