import goodmood from '../images/goodmood.png';
import goodness from '../images/goodness.png';
import hayden from '../images/hayden.png';
import parker from '../images/parker.png';

const brands = [goodmood, goodness, hayden, parker];

const TrustedBrands = () => {
  return (
    <section className="brands container py-5">
      <div className="row text-center">
        <h3 className="cursive-title">Trusted</h3>
        <h1>Brands</h1>
        {brands.map((brand) => (
          <div key={brand} className="col-lg-3">
            <img
              src={brand}
              class="img-fluid"
              alt="brand"
              width="240"
              height="240"
              preserveAspectRatio="xMidYMid slice"
              focusable="false"
            />
          </div>
        ))}
      </div>
    </section>
  );
};

export default TrustedBrands;