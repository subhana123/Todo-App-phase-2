export async function GET() {
  return new Response(JSON.stringify([
    { id: 1, title: 'Demo Task 1', completed: false },
    { id: 2, title: 'Demo Task 2', completed: true }
  ]), { status: 200 });
}
