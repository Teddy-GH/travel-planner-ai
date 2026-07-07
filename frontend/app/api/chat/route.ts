import { ai } from "@/lib/gemini";

export async function POST(request: Request) {
  try {
    const body = await request.json();

    console.log("Request Body:", body);

    const { message } = body;

    console.log("Message:", message);

    const response = await ai.models.generateContent({
      model: "gemini-2.5-flash",
      contents: message,
    });

    console.log("Gemini Response:", response);

    return Response.json({
      reply: response.text,
    });
  } catch (error) {
    console.error("API Error:", error);

    return Response.json(
      {
        error: String(error),
      },
      {
        status: 500,
      }
    );
  }
}