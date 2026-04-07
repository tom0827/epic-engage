import { geoJSONDecode, calculateZoomLevel } from 'components/admin/engagement/form/EngagementWidgets/Map/utils';

describe('Map utils', () => {
    test('decodes valid geojson string', () => {
        const geojsonString = JSON.stringify({
            type: 'FeatureCollection',
            features: [],
        });

        const decoded = geoJSONDecode(geojsonString);

        expect(decoded).toEqual({ type: 'FeatureCollection', features: [] });
    });

    test('decodes double-encoded geojson string', () => {
        const geojsonString = JSON.stringify(
            JSON.stringify({
                type: 'FeatureCollection',
                features: [],
            }),
        );

        const decoded = geoJSONDecode(geojsonString);

        expect(decoded).toEqual({ type: 'FeatureCollection', features: [] });
    });

    test('returns undefined for malformed geojson string', () => {
        const decoded = geoJSONDecode('{not-valid-json}');

        expect(decoded).toBeUndefined();
    });

    test('returns default zoom when geojson is missing', () => {
        expect(calculateZoomLevel(300, 300, undefined)).toBe(12);
    });
});
