import { Box, Container, Typography } from "@mui/material";

const AnalyticsPage = () => (
  <Container sx={{ p: 3 }}>
    <Typography variant="h4" gutterBottom>
      Analytics
    </Typography>
    <Typography color="text.secondary">
      Track your internship funnel performance, conversion rates, and interview success metrics.
    </Typography>
  </Container>
);

export default AnalyticsPage;
