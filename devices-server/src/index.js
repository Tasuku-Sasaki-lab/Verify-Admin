const fastify = require('fastify');
const app = fastify();
const mongoose = require('mongoose');
const deviceAdminRoutes = require('./routes/deviceRoutes');
const deviceUserRoutes = require('./routes/deviceUserRoutes');
const contentRangeHook = require('./hooks/contentRangeHook');
const jwtVerifyHook = require('./hooks/jwtVerifyHook');
const adminRoutes = require('./routes/adminRoutes');
const scepRoutes = require('./routes/scepRoutes');

try {
  const url = process.env.DB_URL
  mongoose.connect(url, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  });
} catch (e) {
  console.error(e);
}

app.decorateRequest('decorded', null);
app.addHook('onRequest', jwtVerifyHook);
app.addHook('preHandler', contentRangeHook);

adminRoutes(app);
deviceAdminRoutes(app);
deviceUserRoutes(app);
scepRoutes(app);

app.listen(5000, (err, address) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  console.log(`Server running on ${address}`);
});